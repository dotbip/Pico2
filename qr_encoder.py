# =============================================================================
# Minimal QR Code Encoder for Compact SeedQR
# =============================================================================
# Implements Version 1 (21x21) QR code with Low error correction
# Specifically designed for 16-byte (128-bit) binary data
# Compatible with SeedSigner/Jade Compact SeedQR format
# =============================================================================

# Reed-Solomon GF(2^8) with primitive polynomial x^8 + x^4 + x^3 + x^2 + 1
# Generator polynomial for 7 EC codewords (Version 1-L)

# Precomputed log/antilog tables for GF(2^8)
GF_EXP = [1] * 512
GF_LOG = [0] * 256

def _init_gf():
    """Initialize Galois Field lookup tables"""
    x = 1
    for i in range(255):
        GF_EXP[i] = x
        GF_LOG[x] = i
        x <<= 1
        if x & 0x100:
            x ^= 0x11d  # Primitive polynomial
    for i in range(255, 512):
        GF_EXP[i] = GF_EXP[i - 255]

_init_gf()

def gf_mul(a, b):
    """Multiply two numbers in GF(2^8)"""
    if a == 0 or b == 0:
        return 0
    return GF_EXP[GF_LOG[a] + GF_LOG[b]]

def rs_encode(data, nsym):
    """Reed-Solomon encode data with nsym error correction symbols"""
    # Generator polynomial coefficients for nsym=7 (Version 1-L)
    # g(x) = (x-α^0)(x-α^1)...(x-α^6)
    gen = [1]
    for i in range(nsym):
        new_gen = [0] * (len(gen) + 1)
        for j, coef in enumerate(gen):
            new_gen[j] ^= coef
            new_gen[j + 1] ^= gf_mul(coef, GF_EXP[i])
        gen = new_gen
    
    # Polynomial division
    result = list(data) + [0] * nsym
    for i in range(len(data)):
        coef = result[i]
        if coef != 0:
            for j, g in enumerate(gen[1:], 1):
                result[i + j] ^= gf_mul(g, coef)
    
    return result[-nsym:]

def create_qr_v2_l(data_bytes):
    """
    Create Version 2 (25x25) QR code with Low error correction.
    Supports up to 32 bytes for 24-word Compact SeedQR.
    
    Args:
        data_bytes: bytes object, max 32 bytes for binary mode
        
    Returns:
        25x25 list of lists (True=black, False=white)
    """
    if len(data_bytes) > 32:
        raise ValueError("Data too long for Version 2-L (max 32 bytes)")
    
    # Initialize 25x25 matrix
    size = 25
    matrix = [[None] * size for _ in range(size)]
    
    # =========================================================================
    # Step 1: Place finder patterns (7x7 at three corners)
    # =========================================================================
    def place_finder(row, col):
        """Place a 7x7 finder pattern"""
        pattern = [
            [1,1,1,1,1,1,1],
            [1,0,0,0,0,0,1],
            [1,0,1,1,1,0,1],
            [1,0,1,1,1,0,1],
            [1,0,1,1,1,0,1],
            [1,0,0,0,0,0,1],
            [1,1,1,1,1,1,1],
        ]
        for r in range(7):
            for c in range(7):
                matrix[row + r][col + c] = bool(pattern[r][c])
    
    # Top-left, top-right, bottom-left
    place_finder(0, 0)
    place_finder(0, 18)
    place_finder(18, 0)
    
    # =========================================================================
    # Step 2: Place separators (white borders around finders)
    # =========================================================================
    # Top-left separator
    for i in range(8):
        if matrix[7][i] is None: matrix[7][i] = False
        if matrix[i][7] is None: matrix[i][7] = False
    
    # Top-right separator
    for i in range(8):
        if matrix[7][17 + i] is None: matrix[7][17 + i] = False
        if matrix[i][17] is None: matrix[i][17] = False
    
    # Bottom-left separator
    for i in range(8):
        if matrix[17][i] is None: matrix[17][i] = False
        if matrix[17 + i][7] is None: matrix[17 + i][7] = False
    
    # =========================================================================
    # Step 3: Place alignment pattern (5x5 at center for Version 2)
    # =========================================================================
    align_pattern = [
        [1,1,1,1,1],
        [1,0,0,0,1],
        [1,0,1,0,1],
        [1,0,0,0,1],
        [1,1,1,1,1],
    ]
    align_row, align_col = 18, 18
    for r in range(5):
        for c in range(5):
            matrix[align_row + r - 2][align_col + c - 2] = bool(align_pattern[r][c])
    
    # =========================================================================
    # Step 4: Place timing patterns
    # =========================================================================
    for i in range(8, 17):
        matrix[6][i] = (i % 2 == 0)
        matrix[i][6] = (i % 2 == 0)
    
    # =========================================================================
    # Step 5: Place dark module (always black)
    # =========================================================================
    matrix[4 * 2 + 9][8] = True  # Version 2 dark module position
    
    # =========================================================================
    # Step 6: Reserve format information areas
    # =========================================================================
    # Around top-left finder
    for i in range(9):
        if matrix[8][i] is None: matrix[8][i] = False
        if matrix[i][8] is None: matrix[i][8] = False
    
    # Around top-right finder
    for i in range(8):
        if matrix[8][17 + i] is None: matrix[8][17 + i] = False
    
    # Around bottom-left finder
    for i in range(7):
        if matrix[18 + i][8] is None: matrix[18 + i][8] = False
    
    # =========================================================================
    # Step 7: Encode data
    # =========================================================================
    data_bits = []
    
    # Mode indicator (4 bits): 0100 for byte mode
    data_bits.extend([0, 1, 0, 0])
    
    # Character count (8 bits for Version 2 byte mode)
    count = len(data_bytes)
    for i in range(7, -1, -1):
        data_bits.append((count >> i) & 1)
    
    # Data bytes
    for byte in data_bytes:
        for i in range(7, -1, -1):
            data_bits.append((byte >> i) & 1)
    
    # Terminator (up to 4 bits)
    terminator_len = min(4, 34 * 8 - len(data_bits))
    data_bits.extend([0] * terminator_len)
    
    # Pad to byte boundary
    while len(data_bits) % 8 != 0:
        data_bits.append(0)
    
    # Convert to bytes
    data_codewords = []
    for i in range(0, len(data_bits), 8):
        byte = 0
        for j in range(8):
            if i + j < len(data_bits):
                byte = (byte << 1) | data_bits[i + j]
        data_codewords.append(byte)
    
    # Pad with alternating 236, 17 to fill 34 data codewords
    pad_bytes = [236, 17]
    pad_idx = 0
    while len(data_codewords) < 34:
        data_codewords.append(pad_bytes[pad_idx % 2])
        pad_idx += 1
    
    # =========================================================================
    # Step 8: Generate error correction codewords (10 for Version 2-L)
    # =========================================================================
    ec_codewords = rs_encode(data_codewords, 10)
    
    # Combine data and EC codewords
    all_codewords = data_codewords + ec_codewords
    
    # Convert to bit stream
    bitstream = []
    for cw in all_codewords:
        for i in range(7, -1, -1):
            bitstream.append((cw >> i) & 1)
    
    # =========================================================================
    # Step 9: Place data bits in zigzag pattern
    # =========================================================================
    bit_idx = 0
    
    # Start from bottom-right, go up in 2-column modules
    col = size - 1
    going_up = True
    
    while col >= 0:
        # Skip timing pattern column
        if col == 6:
            col -= 1
            continue
        
        # Process two columns at a time
        for _ in range(size):
            for c_offset in [0, -1]:
                c = col + c_offset
                if c < 0:
                    continue
                    
                if going_up:
                    r = size - 1 - _
                else:
                    r = _
                
                if matrix[r][c] is None and bit_idx < len(bitstream):
                    matrix[r][c] = bool(bitstream[bit_idx])
                    bit_idx += 1
        
        col -= 2
        going_up = not going_up
    
    # Fill any remaining None with False
    for r in range(size):
        for c in range(size):
            if matrix[r][c] is None:
                matrix[r][c] = False
    
    # =========================================================================
    # Step 10: Apply mask pattern 0 (checkerboard)
    # =========================================================================
    def is_data_module(r, c):
        """Check if module at (r,c) is a data module (not function pattern)"""
        # Finder patterns + separators
        if r < 9 and c < 9: return False  # Top-left
        if r < 9 and c > 16: return False  # Top-right
        if r > 16 and c < 9: return False  # Bottom-left
        # Alignment pattern (16-20, 16-20 for Version 2)
        if 16 <= r <= 20 and 16 <= c <= 20: return False
        # Timing patterns
        if r == 6 or c == 6: return False
        # Format info
        if r == 8 and c < 9: return False
        if r == 8 and c > 16: return False
        if c == 8 and r < 9: return False
        if c == 8 and r > 16: return False
        return True
    
    # Apply mask 0: (row + col) % 2 == 0
    for r in range(size):
        for c in range(size):
            if is_data_module(r, c) and (r + c) % 2 == 0:
                matrix[r][c] = not matrix[r][c]
    
    # =========================================================================
    # Step 11: Place format information
    # =========================================================================
    # Format: EC level L (01) + Mask 0 (000) = 01000
    # After BCH and XOR mask: 111011111000100
    format_bits = [1,1,1,0,1,1,1,1,1,0,0,0,1,0,0]
    
    # Around top-left finder (going right then down)
    format_positions_1 = [
        (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 7), (8, 8),
        (7, 8), (5, 8), (4, 8), (3, 8), (2, 8), (1, 8), (0, 8)
    ]
    
    # Around top-right and bottom-left
    format_positions_2 = [
        (8, 24), (8, 23), (8, 22), (8, 21), (8, 20), (8, 19), (8, 18), (8, 17),
        (18, 8), (19, 8), (20, 8), (21, 8), (22, 8), (23, 8), (24, 8)
    ]
    
    for i, (r, c) in enumerate(format_positions_1):
        matrix[r][c] = bool(format_bits[i])
    
    for i, (r, c) in enumerate(format_positions_2):
        matrix[r][c] = bool(format_bits[i])
    
    return matrix

def create_qr_v1_l(data_bytes):
    """
    Create Version 1 (21x21) QR code with Low error correction.
    
    Args:
        data_bytes: bytes object, max 17 bytes for binary mode
        
    Returns:
        21x21 list of lists (True=black, False=white)
    """
    if len(data_bytes) > 17:
        raise ValueError("Data too long for Version 1-L (max 17 bytes)")
    
    # Initialize 21x21 matrix
    size = 21
    matrix = [[None] * size for _ in range(size)]
    
    # =========================================================================
    # Step 1: Place finder patterns (7x7 at three corners)
    # =========================================================================
    def place_finder(row, col):
        """Place a 7x7 finder pattern"""
        pattern = [
            [1,1,1,1,1,1,1],
            [1,0,0,0,0,0,1],
            [1,0,1,1,1,0,1],
            [1,0,1,1,1,0,1],
            [1,0,1,1,1,0,1],
            [1,0,0,0,0,0,1],
            [1,1,1,1,1,1,1],
        ]
        for r in range(7):
            for c in range(7):
                matrix[row + r][col + c] = bool(pattern[r][c])
    
    # Top-left, top-right, bottom-left
    place_finder(0, 0)
    place_finder(0, 14)
    place_finder(14, 0)
    
    # =========================================================================
    # Step 2: Place separators (white borders around finders)
    # =========================================================================
    # Top-left separator
    for i in range(8):
        if matrix[7][i] is None: matrix[7][i] = False
        if matrix[i][7] is None: matrix[i][7] = False
    
    # Top-right separator
    for i in range(8):
        if matrix[7][13 + i] is None: matrix[7][13 + i] = False
        if matrix[i][13] is None: matrix[i][13] = False
    
    # Bottom-left separator
    for i in range(8):
        if matrix[13][i] is None: matrix[13][i] = False
        if matrix[13 + i][7] is None: matrix[13 + i][7] = False
    
    # =========================================================================
    # Step 3: Place timing patterns
    # =========================================================================
    for i in range(8, 13):
        matrix[6][i] = (i % 2 == 0)
        matrix[i][6] = (i % 2 == 0)
    
    # =========================================================================
    # Step 4: Place dark module (always black)
    # =========================================================================
    matrix[13][8] = True
    
    # =========================================================================
    # Step 5: Reserve format information areas
    # =========================================================================
    # Around top-left finder
    for i in range(9):
        if matrix[8][i] is None: matrix[8][i] = False
        if matrix[i][8] is None: matrix[i][8] = False
    
    # Around top-right finder
    for i in range(8):
        if matrix[8][13 + i] is None: matrix[8][13 + i] = False
    
    # Around bottom-left finder  
    for i in range(7):
        if matrix[14 + i][8] is None: matrix[14 + i][8] = False
    
    # =========================================================================
    # Step 6: Encode data
    # =========================================================================
    # Mode indicator: 0100 (byte mode)
    # Character count: 8 bits for Version 1
    # Data: actual bytes
    # Terminator: 0000
    
    data_bits = []
    
    # Mode indicator (4 bits): 0100 for byte mode
    data_bits.extend([0, 1, 0, 0])
    
    # Character count (8 bits for V1 byte mode)
    count = len(data_bytes)
    for i in range(7, -1, -1):
        data_bits.append((count >> i) & 1)
    
    # Data bytes
    for byte in data_bytes:
        for i in range(7, -1, -1):
            data_bits.append((byte >> i) & 1)
    
    # Terminator (up to 4 bits)
    terminator_len = min(4, 19 * 8 - len(data_bits))
    data_bits.extend([0] * terminator_len)
    
    # Pad to byte boundary
    while len(data_bits) % 8 != 0:
        data_bits.append(0)
    
    # Convert to bytes
    data_codewords = []
    for i in range(0, len(data_bits), 8):
        byte = 0
        for j in range(8):
            if i + j < len(data_bits):
                byte = (byte << 1) | data_bits[i + j]
        data_codewords.append(byte)
    
    # Pad with alternating 236, 17 to fill 19 data codewords
    pad_bytes = [236, 17]
    pad_idx = 0
    while len(data_codewords) < 19:
        data_codewords.append(pad_bytes[pad_idx % 2])
        pad_idx += 1
    
    # =========================================================================
    # Step 7: Generate error correction codewords
    # =========================================================================
    ec_codewords = rs_encode(data_codewords, 7)
    
    # Combine data and EC codewords
    all_codewords = data_codewords + ec_codewords
    
    # Convert to bit stream
    bitstream = []
    for cw in all_codewords:
        for i in range(7, -1, -1):
            bitstream.append((cw >> i) & 1)
    
    # =========================================================================
    # Step 8: Place data bits in zigzag pattern
    # =========================================================================
    bit_idx = 0
    
    # Start from bottom-right, go up in 2-column modules
    col = size - 1
    going_up = True
    
    while col >= 0:
        # Skip timing pattern column
        if col == 6:
            col -= 1
            continue
        
        # Process two columns at a time
        for _ in range(size):
            for c_offset in [0, -1]:
                c = col + c_offset
                if c < 0:
                    continue
                    
                if going_up:
                    r = size - 1 - (_ if c_offset == 0 else _)
                else:
                    r = _ if c_offset == 0 else _
                
                # Recalculate row based on direction
                if going_up:
                    r = size - 1 - _
                else:
                    r = _
                
                if matrix[r][c] is None and bit_idx < len(bitstream):
                    matrix[r][c] = bool(bitstream[bit_idx])
                    bit_idx += 1
        
        col -= 2
        going_up = not going_up
    
    # Fill any remaining None with False
    for r in range(size):
        for c in range(size):
            if matrix[r][c] is None:
                matrix[r][c] = False
    
    # =========================================================================
    # Step 9: Apply mask pattern 0 (checkerboard)
    # =========================================================================
    def is_data_module(r, c):
        """Check if module at (r,c) is a data module (not function pattern)"""
        # Finder patterns + separators
        if r < 9 and c < 9: return False  # Top-left
        if r < 9 and c > 12: return False  # Top-right
        if r > 12 and c < 9: return False  # Bottom-left
        # Timing patterns
        if r == 6 or c == 6: return False
        # Format info
        if r == 8 and c < 9: return False
        if r == 8 and c > 12: return False
        if c == 8 and r < 9: return False
        if c == 8 and r > 12: return False
        return True
    
    # Apply mask 0: (row + col) % 2 == 0
    for r in range(size):
        for c in range(size):
            if is_data_module(r, c) and (r + c) % 2 == 0:
                matrix[r][c] = not matrix[r][c]
    
    # =========================================================================
    # Step 10: Place format information
    # =========================================================================
    # Format: EC level L (01) + Mask 0 (000) = 01000
    # After BCH and XOR mask: 111011111000100
    format_bits = [1,1,1,0,1,1,1,1,1,0,0,0,1,0,0]
    
    # Around top-left finder (going right then down)
    format_positions_1 = [
        (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 7), (8, 8),
        (7, 8), (5, 8), (4, 8), (3, 8), (2, 8), (1, 8), (0, 8)
    ]
    
    # Around top-right and bottom-left
    format_positions_2 = [
        (8, 20), (8, 19), (8, 18), (8, 17), (8, 16), (8, 15), (8, 14), (8, 13),
        (14, 8), (15, 8), (16, 8), (17, 8), (18, 8), (19, 8), (20, 8)
    ]
    
    for i, (r, c) in enumerate(format_positions_1):
        matrix[r][c] = bool(format_bits[i])
    
    for i, (r, c) in enumerate(format_positions_2):
        matrix[r][c] = bool(format_bits[i])
    
    return matrix


def grid_to_compact_seedqr(*args, **kwargs):
    raise RuntimeError("This function is disabled. QR must be generated from mnemonic words.")
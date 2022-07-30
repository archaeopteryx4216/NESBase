; PPU Registers
PPUCTRL          = $2000        ; PPU Control flags (Write)
PPUCTRL_V_MASK   = %10000000    ; NMI at VBlank Enable
PPUCTRL_H_MASK   = %00100000    ; Sprite size (0=>8x8, 1=>16x16)
PPUCTRL_B_MASK   = %00010000    ; BG Pattern Address (0=>$0000, 1=>$1000)
PPUCTRL_S_MASK   = %00001000    ; 8x8 sprite pattern address (0=>$0000, 1=>$1000)
PPUCTRL_I_MASK   = %00000100    ; VRAM Address increment (0=>1, 1=>32)
PPUCTRL_NN_MASK  = %00000011    ; Nametable Page Select (0=>$2000, 1=>$2400, 2=>$2800, 3=>$2c00)

PPUMASK          = $2001        ; More PPU Control flags (Write)
PPUMASK_BGR_MASK = %11100000    ; RGB Emphasis (bit 7 => blue, bit 6 => green, bit 5 => red)
PPUMASK_SE_MASK  = %00010000    ; Sprite Enable
PPUMASK_BE_MASK  = $00001000    ; Background Enable
PPUMASK_LCE_MASK = $00000100    ; Show Sprites in leftmost 8 pixels
PPUMASK_RCE_MASK = $00000010    ; Show Sprites in rightmost 8 pixels
PPUMASK_G_MASK   = $00000001    ; Greyscale (0=>Color, 1=>Greyscale)

PPUSTATUS             = $2002       ; PPU Status plags (Read)
PPUSTATUS_VBLANK_MASK = $10000000   ; VBlank has started (reset after read)
PPUSTATUS_SZH_MASK    = $01000000   ; Sprite 0 intersects background
PPUSTATUS_SOF_MASK    = $00100000   ; Sprite overflow

OAMADDR = $2003

OAMDATA = $2004

PPUSCROLL = $2005

PPUADDR = $2006

PPUDATA = $2007

OAMDMA = $4014


; APU Registers
PULSEA0 = $4000
PULSEA1 = $4001
PULSEA2 = $4002
PULSEA3 = $4003

PULSEB0 = $4004
PULSEB1 = $4005
PULSEB2 = $4006
PULSEB3 = $4007

TRIANG0 = $4008
TRIANG1 = $400A
TRIANG2 = $400B

NOISE0 = $400C
NOISE1 = $400E
NOISE2 = $400F

DMC0 = $4010
DMC1 = $4011
DMC2 = $4012
DMC3 = $4013
DMC4 = $4015
DMC5 = $4017
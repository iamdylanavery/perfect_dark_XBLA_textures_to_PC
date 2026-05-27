
# Perfect Dark: XBLA to PC Port Texture Bridge

This repository contains a lightweight Python script to convert and remap the high-definition textures from the Xbox Live Arcade (XBLA) port of *Perfect Dark* so they can be loaded natively into the decompiled PC Port by `fgsfdsfgs` and with the External HD Textures mod by `rafccq`.

## How It Works

The XBLA remaster of *Perfect Dark* was natively recompiled from the original N64 source code by 4J Studios. Rather than rewriting the texture rendering engine, they preserved the original texture array mapping. 

The first 3,502 textures in the XBLA assets line up 1:1 with the original N64 texture array. The N64 game references these assets using 4-digit hexadecimal addresses (e.g., `00F0`), which are simply the hexadecimal equivalent of their decimal array indices (e.g., 240). 

By extracting the XBLA assets, unswizzling them, and converting their decimal array IDs back into 4-digit hexadecimal, we can wire the HD textures directly into the PC Port's `data/ext_tex/` folder.

---

## Prerequisites

1. **Python 3**: Installed on your system (Windows, macOS, or Linux/Steam Deck).
2. **Pillow Library**: Python's imaging library used to convert the DDS files to PNG.
3. **Noesis**: Used to run the initial extraction plugin.

---

## Step-by-Step Installation

### Step 1: Extract Your Textures
1. Download **Noesis** (a portable tool for asset viewing and exporting).
2. Copy the community Noesis plugin `fmt_PerfectDarkXBLA.py` (by Dodylectable) and drop it into your `Noesis/plugins/python/` folder.
3. Run Noesis, navigate to your XBLA `Textures.raw` file, right-click the archive, select **Export**, and choose `.dds` as your output. 
4. This will generate a folder named `Textures_files` full of unswizzled `.dds` files named like:
   `tex_0240_fmt_82_256x256_parent_4294967295.dds`

### Step 2: Install dependencies
Open your terminal or Command Prompt/PowerShell and install the Pillow library:

pip install Pillow

### Step 3: Run the Bridge Script

1.  Download the pd_final_bridge.py script from this repository.
2.  Place the pd_final_bridge.py file right next to your newly generated
    Textures_files directory.
3.  Run the script:
    python pd_final_bridge.py
4.  The script will automatically parse the decimal indices, convert them to
    uppercase 4-digit N64 hex codes, and batch convert the DDS files to PNGs.

### Step 4: Import Into the PC Port

1.  Open the newly created ext_tex_ready directory.
2.  Copy all the .png (and fallback .dds files, if any).
3.  Paste them directly into your decompiled Perfect Dark PC Port's
    data/ext_tex/ directory.
4.  Launch the game and enjoy!

### Credits

  - Dodylectable - Developed the Noesis Python extraction plugin mapping the
    base offsets and unswizzle matrices.
  - kholdfuzion, shalashaka, tjoener, neptuwunium - For early file format
    reverse-engineering research.


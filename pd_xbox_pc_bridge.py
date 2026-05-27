import os
import shutil
try:
    from PIL import Image
except ImportError:
    print("Pillow is not installed! Run: pip3 install Pillow")
    exit()

def bridge_to_pc_port(in_dir, out_dir):
    print("=======================================================")
    print("    PERFECT DARK: THE FINAL XBLA -> PC PORT BRIDGE     ")
    print("=======================================================\n")
    
    if not os.path.exists(in_dir):
        print(f"[ERROR] Could not find input directory: {in_dir}")
        return
        
    os.makedirs(out_dir, exist_ok=True)
    
    files = [f for f in os.listdir(in_dir) if f.startswith('tex_') and f.endswith('.dds')]
    print(f"Found {len(files)} XBLA DDS textures. Mapping to N64 Hex Codes...\n")
    
    success = 0
    errors = 0
    
    for filename in files:
        # Expected filename: tex_0240_fmt_82_256x256_parent_4294967295.dds
        parts = filename.split('_')
        
        try:
            # Extract the decimal index (e.g., "0240" -> 240)
            dec_id = int(parts[1])
        except ValueError:
            print(f"[SKIP] Could not parse index from {filename}")
            continue
            
        # Convert decimal index to 4-digit uppercase Hex (e.g., 240 -> "00F0")
        hex_id = f"{dec_id:04X}"
        out_png = os.path.join(out_dir, f"{hex_id}.png")
        in_dds = os.path.join(in_dir, filename)
        
        try:
            # Convert DDS to PNG on the fly for the PC Port
            with Image.open(in_dds) as img:
                img.save(out_png)
            success += 1
            
            if success % 500 == 0:
                print(f"Mapped and converted {success} textures...")
                
        except Exception as e:
            # If Pillow fails to read a specific DDS format (like raw ARGB), copy it as DDS instead
            out_dds_fallback = os.path.join(out_dir, f"{hex_id}.dds")
            shutil.copy(in_dds, out_dds_fallback)
            errors += 1
            
    print("=======================================================")
    print("                  BRIDGE COMPLETE!                     ")
    print("=======================================================")
    print(f"Successfully converted {success} textures to PNG.")
    if errors > 0:
        print(f"Copied {errors} textures as DDS (Pillow couldn't convert them).")
    print(f"\nYour files are waiting in '{out_dir}'.")
    print("Drop them directly into your PC Port's ext_tex folder!")

if __name__ == '__main__':
    # Make sure these match your folder names
    INPUT_FOLDER = './Textures_files'
    OUTPUT_FOLDER = './ext_tex_ready'
    
    bridge_to_pc_port(INPUT_FOLDER, OUTPUT_FOLDER)

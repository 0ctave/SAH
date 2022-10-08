import cairo
from desmume.emulator import DeSmuME, DeSmuME_Savestate, SCREEN_PIXEL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT
from PIL import Image, ImageEnhance


def run_emulation():
    emu = DeSmuME()
    emu.open('rom/0201eumkds.nds')

    savestate = DeSmuME_Savestate(emu)
    savestate.load_file('saves/1.dst')

    # Create the window for the emulator
    # window = emu.create_sdl_window()

    i = 0
    # Run the emulation as fast as possible until quit
    while True:
        # window.process_input()   # Controls are the default DeSmuME controls, see below.

        emu.cycle()

        if i % 10 == 0:
            gpu_framebuffer = emu.display_buffer_as_rgbx()
            upper_image = cairo.ImageSurface.create_for_data(gpu_framebuffer[:SCREEN_PIXEL_SIZE * 4],
                                                             cairo.FORMAT_RGB24, SCREEN_WIDTH, SCREEN_HEIGHT)
            upper_image.write_to_png("images/origin" + str(i) + ".png")
            img = Image.open("images/origin" + str(i) + ".png")

            img = img.resize((int(SCREEN_WIDTH / 6), int(SCREEN_HEIGHT / 6)), Image.ANTIALIAS)
            img = img.convert("L")

            img.save('images/resized_image' + str(i) + '.jpg')

            lower_image = cairo.ImageSurface.create_for_data(
                gpu_framebuffer[SCREEN_PIXEL_SIZE * 4:], cairo.FORMAT_RGB24, SCREEN_WIDTH, SCREEN_HEIGHT
            )

            lower_image.write_to_png('images/lower' + str(i) + '.png')

        i = i + 1
        # -- Do your custom stuff here, or use memory hooks.

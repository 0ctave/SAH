from desmume.emulator import DeSmuME, DeSmuME_Savestate

def run_emulation():

    emu = DeSmuME()
    emu.open('rom/0201eumkds.nds')

    savestate = DeSmuME_Savestate(emu)
    savestate.load_file('saves/1.dst')

    # Create the window for the emulator
    window = emu.create_sdl_window()

    # Run the emulation as fast as possible until quit
    while not window.has_quit():
        window.process_input()   # Controls are the default DeSmuME controls, see below.


        emu.cycle()
        window.draw()

        # -- Do your custom stuff here, or use memory hooks.
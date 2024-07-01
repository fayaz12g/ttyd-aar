
def create_visuals(do_graphics_increase, do_120fps, do_60fps):

    graphics = "disabled"
    fps60 = "disabled"
    fps120 = "disabled"

    do_island = False
    
    visual_fixes = []

    if do_graphics_increase:
        graphics = "enabled"
    if do_60fps:
        fps60 = "enabled"
    if do_120fps:
        fps120 = "enabled"
        
    visuals1_0_0 = f'''// Improved LOD
@{graphics}
0020451c 00D0351E
@stop

// 60 FPS Mode
@{fps60}
00204740 35008052
002e75c0 08C1881A
0059b634 A820A872
@stop

// 3440x1440 Docked 1280x720 Handheld
@{fps120}
0030A010 A81AA852
0030ee34 09B48052
0030ee38 08AE8152
0030ec74 09AE8152
0030ec80 0AB48052
0030ed70 09AE8152
0030ed7c 0AB48052
0030eb88 09A08052
0030eb94 0A5A8052
0030edec 09A08052
0030edf8 0A5A8052
0030e29c 02B48052
0030e2a0 01AE8152
0030e558 04B48052
0030e564 03AE8152
00364844 08AE8152
0036484c 0AB48052
0030fa10 09AE8152
0030fa18 0AB48052
0030a86c 08AE81D2
0030a878 08B4C0F2
0030a03c 08B48052
0030a04c 09AEC1F2
0030fa0c EBAAA852
0030fa1c 8B96A852
00331374 0AAE8152
003313c4 0AB48052
@stop
'''


    visual_fixes.append(visuals1_0_0)

    
    return visual_fixes
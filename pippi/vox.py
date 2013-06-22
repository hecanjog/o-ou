from pippi import dsp
import fx

vriffs = ['01', '02', '03', '05', '06', '07']
vriffs = [ dsp.read('vox_%s.wav' % v).data for v in vriffs ]
#vdrone = dsp.read('vox_04_drone.wav').data

beat = dsp.bpm2frames(125)
print dsp.fts(beat)

out = ''
for loop in range(12):
    loops = dsp.randshuffle(vriffs)

    for i, l in enumerate(loops):
        l = [ dsp.cut(l, dsp.randint(0, dsp.flen(l) - (beat)), beat) for s in range(16) ]
        l = [ dsp.pan(seg, dsp.rand()) for seg in l ]
        l = [ dsp.env(seg, 'random') for seg in l ]
        loops[i] = ''.join(l)

    out += dsp.mix(loops)

dsp.write(out, 'vox_pulses02')


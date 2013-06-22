from pippi import dsp
import orc, pat, fx

drums = [ orc.clap, orc.hihat, orc.kick ]

out = ''
beat = dsp.bpm2frames(125) / 2

for bar in range(8):
    perc = ''
    for i in range(32):
        if dsp.randint(0, 2) == 0:
            perc += dsp.randchoose(drums)(dsp.rand(), beat)
        else:
            perc += dsp.pad('', beat, 0)

    kick = orc.kick(1, beat * 32)

    out += dsp.mix([ perc, kick ])

dsp.write(out, 'drums')

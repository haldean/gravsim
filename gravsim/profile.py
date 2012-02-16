import cProfile
import pstats
import gravsim

print('Profiling...')
cProfile.run('gravsim.main()', 'gprof')
stats = pstats.Stats('gprof')
stats.strip_dirs().sort_stats('time').print_stats(1.0)

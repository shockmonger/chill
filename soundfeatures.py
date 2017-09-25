import essentia

  # as there are 2 operating modes in essentia which have the same algorithms,
  # these latter are dispatched into 2 submodules:
import essentia.standard
import essentia.streaming

basefile = '/home/tejaswik/Documents/CurrentProjects/chills/'

  # let's have a look at what is in there
  #print dir(essentia.standard)
def loadsound(stri):
	fil = basefile+parts[i]+songs[j]
	loader = essentia.standard.Monoloader(filename = fil)
	audio = loader()

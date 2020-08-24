## The IP address the notebook server will listen on.
c.NotebookApp.ip = '0.0.0.0'

## The directory to use for notebooks and kernels.
c.NotebookApp.notebook_dir = '../jupyter'

## Whether to open in a browser after starting. The specific browser used is
#  platform dependent and determined by the python standard library `webbrowser`
#  module, unless it is overridden using the --browser (NotebookApp.browser)
#  configuration option.
c.NotebookApp.open_browser = False

## Hashed password to use for web authentication.
#  
#  To generate, type in a python/IPython shell:
#  
#    from notebook.auth import passwd; passwd()
#  
#  The string should be of the form type:salt:hashed-password.
c.NotebookApp.password = 'sha1:5caa8e7be44d:c8e0d0dc2e3d662e96eed8613b669dc12585eb65'

## The port the notebook server will listen on.
c.NotebookApp.port = 8888

## Shut down the server after N seconds with no kernels or terminals running and
#  no activity. This can be used together with culling idle kernels
#  (MappingKernelManager.cull_idle_timeout) to shutdown the notebook server when
#  it's not in use. This is not precisely timed: it may shut down up to a minute
#  later. 0 (the default) disables this automatic shutdown.
c.NotebookApp.shutdown_no_activity_timeout = 604800

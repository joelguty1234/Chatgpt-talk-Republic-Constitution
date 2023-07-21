import sys
from cx_Freeze import setup, Executable

options = {
    'build_exe': {
        'packages': ['onnxruntime', 'chromadb.telemetry.posthog',
                     'chromadb.api.segment','chromadb.db.impl',
                     'chromadb.db.impl.sqlite','chromadb.migrations',
                     'chromadb.migrations.embeddings_queue',
                     'chromadb.segment.impl.manager.local',
                     'chromadb.segment.impl.vector.local_hnsw',
                     'chromadb.segment.impl.metadata.sqlite','tiktoken_ext',
                     ], 
        'include_files': ['../frontend.ui', '../images/'],
    }
}
base = "Win32GUI" if sys.platform == "win32" else None

setup(name = "GeeksforGeeks" ,
      version = "0.2" ,
      description = "" ,
      options=options,
      executables = [Executable("../guiu.py", base=base)])
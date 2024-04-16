 
PS C:\Users\lucia\Desktop\semana03>  c:; cd 'c:\Users\lucia\Desktop\semana03'; & 'c:\Users\lucia\AppData\Local\Programs\Python\Python312\python.exe' 'c:\Users\lucia\.vscode\extensions\ms-python.debugpy-2024.4.0-win32-x64\bundled\libs\debugpy\adapter/../..\debugpy\launcher' '63549' '--' 'C:\Users\lucia\Desktop\semana03\exercicio1.py' 
Traceback (most recent call last):
  File "c:\Users\lucia\AppData\Local\Programs\Python\Python312\Lib\runpy.py", line 198, in _run_module_as_main
    return _run_code(code, main_globals, None,
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Users\lucia\AppData\Local\Programs\Python\Python312\Lib\runpy.py", line 88, in _run_code
    exec(code, run_globals)
  File "c:\Users\lucia\.vscode\extensions\ms-python.debugpy-2024.4.0-win32-x64\bundled\libs\debugpy\adapter/../..\debugpy\launcher/../..\debugpy\__main__.py", line 39, in <module>
    cli.main()
  File "c:\Users\lucia\.vscode\extensions\ms-python.debugpy-2024.4.0-win32-x64\bundled\libs\debugpy\adapter/../..\debugpy\launcher/../..\debugpy/..\debugpy\server\cli.py", line 430, in main
    run()
  File "c:\Users\lucia\.vscode\extensions\ms-python.debugpy-2024.4.0-win32-x64\bundled\libs\debugpy\adapter/../..\debugpy\launcher/../..\debugpy/..\debugpy\server\cli.py", line 284, in run_file
    runpy.run_path(target, run_name="__main__")
  File "c:\Users\lucia\.vscode\extensions\ms-python.debugpy-2024.4.0-win32-x64\bundled\libs\debugpy\_vendored\pydevd\_pydevd_bundle\pydevd_runpy.py", line 320, in run_path
    code, fname = _get_code_from_file(run_name, path_name)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pydevd_runpy.py", line 294, in _get_code_from_file
    code = compile(f.read(), fname, 'exec')
    print("Passo 2: Após isso acrescente o creme de leite, esse passo importante pois o creme de leite e o pó não se misturam facilmente)                                                                               ó não se misturam facilm
          ^
SyntaxError: unterminated string literal (detected at line 15)
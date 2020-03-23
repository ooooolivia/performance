dotnet run -c Release -- ^
--app-exe dotnet ^
--metric-type TimeToMain ^
--trace-file-name test-linux-collect-1 ^
--app-args "build" ^
--log-file-name "linux-collect-1.log" ^
--working-dir  C:\Users\bache\repos\performance-linux-tracing\src\scenarios\emptyconsoletemplate\app ^
--process-will-exit ^
--gui-app false
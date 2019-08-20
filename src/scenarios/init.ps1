$scripts = Join-Path $PSScriptRoot '..\..\scripts\' -Resolve
$shared = Join-Path $PSScriptRoot 'shared' -Resolve
$env:PYTHONPATH="$scripts;$PSScriptRoot;$shared"

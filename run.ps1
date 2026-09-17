$natsServerProcess = Start-Process -FilePath "nats-server" -PassThru
Start-Sleep -Seconds 1

try{
    ./setup.ps1
    uv run -m satellite
}
finally{
    Stop-Process -Id $natsServerProcess.Id -Force -ErrorAction SilentlyContinue
}

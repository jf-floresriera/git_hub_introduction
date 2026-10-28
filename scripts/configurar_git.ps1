# Configuración inicial de Git en Windows (PowerShell).
# Uso:  powershell -ExecutionPolicy Bypass -File scripts\configurar_git.ps1

$ErrorActionPreference = "Stop"

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "Git no está instalado. Instálalo con:" -ForegroundColor Yellow
    Write-Host "  winget install --id Git.Git -e --source winget"
    exit 1
}

Write-Host "Git encontrado: $(git --version)" -ForegroundColor Green
Write-Host ""

$nombreActual = git config --global user.name
$correoActual = git config --global user.email

$nombre = Read-Host "Nombre completo [$nombreActual]"
$correo = Read-Host "Correo registrado en GitHub [$correoActual]"
if ([string]::IsNullOrWhiteSpace($nombre)) { $nombre = $nombreActual }
if ([string]::IsNullOrWhiteSpace($correo)) { $correo = $correoActual }

if ([string]::IsNullOrWhiteSpace($nombre) -or [string]::IsNullOrWhiteSpace($correo)) {
    Write-Host "Nombre y correo son obligatorios." -ForegroundColor Red
    exit 1
}

git config --global user.name "$nombre"
git config --global user.email "$correo"
git config --global init.defaultBranch main
git config --global pull.rebase false
git config --global core.autocrlf true
git config --global color.ui auto

Write-Host ""
Write-Host "Configuración guardada:" -ForegroundColor Green
git config --global --list | Select-String -Pattern "^(user|init|pull|core.autocrlf)"

Write-Host ""
if (Get-Command gh -ErrorAction SilentlyContinue) {
    gh auth status 2>$null | Out-Null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "GitHub CLI ya tiene una sesión activa."
    } else {
        $r = Read-Host "¿Iniciar sesión en GitHub ahora con 'gh auth login'? [s/N]"
        if ($r -eq "s") { gh auth login }
    }
} else {
    Write-Host "Sugerencia: instala GitHub CLI para autenticarte fácilmente:"
    Write-Host "  winget install --id GitHub.cli -e"
}

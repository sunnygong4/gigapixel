# Generate DZI tiles using vips (if installed via Chocolatey)
# Usage: .\generate-tiles.ps1 image.jpg
#        .\generate-tiles.ps1 image1.jpg, image2.jpg

param(
    [Parameter(Mandatory=$true, ValueFromRemainingArguments=$true)]
    [string[]]$Images,

    [string]$OutputDir = "images"
)

$vips = Get-Command vips -ErrorAction SilentlyContinue
if (-not $vips) {
    Write-Error "vips not found. Install with: choco install vips"
    exit 1
}

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

foreach ($img in $Images) {
    if (-not (Test-Path $img)) {
        Write-Warning "Skipping $img - not found"
        continue
    }

    $name = [System.IO.Path]::GetFileNameWithoutExtension($img)
    $outFolder = Join-Path $OutputDir $name
    New-Item -ItemType Directory -Force -Path $outFolder | Out-Null

    Write-Host "Processing $img -> $outFolder/"
    & vips dzsave $img "$outFolder\$name" --tile-size 256 --overlap 1 --suffix .jpg

    # Create thumbnail
    $thumbPath = Join-Path $outFolder "thumb.jpg"
    & vips thumbnail $img $thumbPath 1024 --height 768
}

Write-Host "`nDone! Add your photos to photos.js"

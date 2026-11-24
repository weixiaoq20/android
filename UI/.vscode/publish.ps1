# 同步 Desktop\UI 到 android 仓库并推送到 GitHub
$ErrorActionPreference = "Stop"
$src = "C:\Users\Administrator\Desktop\UI"
$repo = "C:\Users\Administrator\Desktop\_android-repo"
$dst = Join-Path $repo "UI"

if (-not (Test-Path $repo)) { throw "找不到仓库: $repo" }

Write-Host "同步文件..."
Copy-Item -Path (Join-Path $src "*") -Destination $dst -Recurse -Force

Set-Location $repo
git add UI/
$status = git status --porcelain
if (-not $status) {
  Write-Host "没有变更，无需发布。"
  exit 0
}

git status -sb
git commit -m "Publish latest UI from Desktop."
git push origin master
Write-Host "已发布: https://weixiaoq20.github.io/android/UI/fujugongxiang-miniapp/home.html"
git log -1 --oneline

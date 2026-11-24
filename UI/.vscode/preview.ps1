# 打开福聚贡翔小程序首页（默认运行 / 打开文件夹时自动执行）
$homePage = "C:\Users\Administrator\Desktop\UI\fujugongxiang-miniapp\home.html"
if (-not (Test-Path -LiteralPath $homePage)) {
  Write-Error "找不到页面: $homePage"
  exit 1
}
Start-Process -FilePath $homePage
Write-Host "已打开: $homePage"

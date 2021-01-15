var deviceWidth = document.documentElement.clientWidth || window.innerWidth;
var deviceHeight = document.documentElement.clientHeight || window.innerHeight;
// console.log(deviceWidth, deviceHeight);
if (deviceWidth >= 1920) {
  deviceWidth = 1920;
}
document.documentElement.style.fontSize = deviceWidth / 19.2 + "px";

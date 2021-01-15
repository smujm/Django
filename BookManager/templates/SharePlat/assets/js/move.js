//  接收的方法

function onDragOver(even) {
  even.preventDefault();
}
function onDrop(even) {
  even.dataTransfer.setData("Text", even.target.id);
}

function onDragStart(even) {
  even.preventDefault();

  var data = even.dataTransfer.getData("Text");

  var item = document.getElementById(data).cloneNode();

  even.target.appendChild(item);
}

// how to make charts dynamic? 

// var myCanvas = document.getElementById("myCanvas");
// myCanvas.width = 300;
// myCanvas.height = 300;
  
// var ctx = myCanvas.getContext("2d");

$('.value').each(function() {
	var text = $(this).text();
	$(this).parent().css('width', text);
});

$('.block').tooltip();
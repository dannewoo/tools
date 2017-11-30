$(document).ready(function() {
	function shuffle(array) {
	  var currentIndex = array.length, temporaryValue, randomIndex ;

	  // While there remain elements to shuffle...
	  while (0 !== currentIndex) {

	    // Pick a remaining element...
	    randomIndex = Math.floor(Math.random() * currentIndex);
	    currentIndex -= 1;

	    // And swap it with the current element.
	    temporaryValue = array[currentIndex];
	    array[currentIndex] = array[randomIndex];
	    array[randomIndex] = temporaryValue;
	  }
	  return array;
	}

	var students = ["Shyan", "Alexandra Brasher", "Kira Chan", "Jennifer Dong", "Alex Erazo",
	"Byron", "Ryan", "Justin", "Giancarlo", "Monica", "Nick", "Amy",
	"Jennifer Stryjewski", "Doum Suh", "Emma", "Gloria", "Brian", "Chanel", "Tiffany"]

	shuffle(students);

	// for (var i = 0; i < students.length; i++) {
	// 	$("body").append("<p>" + students[i] + "</p>");
	// }
	i = 0;
	$("#btn").click(function(){
		$("body").append("<p>" + students[i] + "</p>");
		i++;

	})


	
	console.log(students);
})


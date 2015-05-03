var randomScalingFactor = function(){ return Math.round(Math.random()*1000000)};

	var lineChartData = {
			labels  : ["January","February","March","April","May"],
			datasets : [
				//government values
				{
					label: "My First dataset",
					fillColor : "rgba(220,220,220,0.2)",
					strokeColor : "rgba(220,220,220,1)",
					pointColor : "rgba(220,220,220,1)",
					pointStrokeColor : "#fff",
					pointHighlightFill : "#fff",
					pointHighlightStroke : "rgba(220,220,220,1)",
					data : [60000,61020,65000,70000,71500]
				},
				//hostel values
				{
					label: "My Second dataset",
					fillColor : "rgba(48, 164, 255, 0.2)",
					strokeColor : "rgba(48, 164, 255, 1)",
					pointColor : "rgba(48, 164, 255, 1)",
					pointStrokeColor : "#fff",
					pointHighlightFill : "#fff",
					pointHighlightStroke : "rgba(48, 164, 255, 1)",
					data : [62000,68040,67040,71500,80000]
				}
			]

		}

	var barChartData = {
			labels : ["January","February","March","April","May"],
			datasets : [
				{
					fillColor : "rgba(220,220,220,0.5)",
					strokeColor : "rgba(220,220,220,0.8)",
					highlightFill: "rgba(220,220,220,0.75)",
					highlightStroke: "rgba(220,220,220,1)",
					data : [60000,61020,65000,70000,71500]
				},
				{
					fillColor : "rgba(48, 164, 255, 0.2)",
					strokeColor : "rgba(48, 164, 255, 0.8)",
					highlightFill : "rgba(48, 164, 255, 0.75)",
					highlightStroke : "rgba(48, 164, 255, 1)",
					data : [62000,68040,67040,71500,80000]
				}
			]

		}

	//percentage consumption per floor
	var pieData = [
				{
					value: 10238,
					color:"#30a5ff",
					highlight: "#62b9fb",
					label: "Ground Floor"
				},
				{
					value: 16302,
					color: "#ffb53e",
					highlight: "#fac878",
					label: "First Floor"
				},
				{
					value: 17889,
					color: "#1ebfae",
					highlight: "#3cdfce",
					label: "Second Floor"
				},
				{
					value: 19289,
					color: "#f9243f",
					highlight: "#f6495f",
					label: "Third Floor"
				},
				{
					value: 15739,
					color: "#19A319",
					highlight: "#80CC80",
					label: "Fourth Floor"
				}

			];

	//percentage consumption per wing
	var doughnutData = [
					{
						value: 38728,
						color: "#ffb53e",
						highlight: "#fac878",
						label: "A + B/2 Wing"
					},
					{
						value: 43812,
						color: "#1ebfae",
						highlight: "#3cdfce",
						label: "B/2 + C Wing"
					}

				];

window.onload = function(){
	var chart1 = document.getElementById("line-chart").getContext("2d");
	window.myLine = new Chart(chart1).Line(lineChartData, {
		responsive: true
	});
	var chart2 = document.getElementById("bar-chart").getContext("2d");
	window.myBar = new Chart(chart2).Bar(barChartData, {
		responsive : true
	});
	var chart3 = document.getElementById("doughnut-chart").getContext("2d");
	window.myDoughnut = new Chart(chart3).Doughnut(doughnutData, {responsive : true
	});
	var chart4 = document.getElementById("pie-chart").getContext("2d");
	window.myPie = new Chart(chart4).Pie(pieData, {responsive : true
	});

};

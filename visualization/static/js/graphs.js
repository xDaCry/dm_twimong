queue()
    .defer(d3.json, "/data/tweets")
    .await(makeGraphs);

function makeGraphs(error, projectsJson) {

	//Clean projectsJson data
	var donorschooseProjects = projectsJson;

	//Create a Crossfilter instance
	var ndx = crossfilter(donorschooseProjects);

	//Define Dimensions
	var langDim = ndx.dimension(function(d) { return d["lang"]; });

	//Calculate metrics
	var langGroup = langDim.group();
    var langGroupTop = getTops(langGroup);

	var all = ndx.groupAll();

    //Charts
	var langTypeChart = dc.rowChart("#resource-type-row-chart");
	var numberTweets = dc.numberDisplay("#number-projects-nd");

	numberTweets
		.formatNumber(d3.format("d"))
		.valueAccessor(function(d){return d; })
		.group(all);

	langTypeChart
        .width(300)
        .height(250)
        .dimension(langDim)
        .group(langGroupTop)
        .xAxis().ticks(4);


    dc.renderAll();

    function getTops(source_group) {
    return {
        all: function () {
            return source_group.top(5);
        }
    };
    }
        setInterval(function(){
        //dc.renderAll();
        dc.redrawAll();
        //window.location.reload(1);
    }, 5000);
};
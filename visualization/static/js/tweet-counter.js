function tweetCountPieChart(chartSelector) {
  var count = 0;
  var svg;

    createBarChart();

  function createBarChart(){
    createChart();
    startBarChartUpdateTimer();
  }

  function createChart(){
  svg = d3.select(chartSelector)
          .append("text")
          .attr("width", 100)
          .attr("height", 100)
          .text(count);
  }

  function startBarChartUpdateTimer() {
    setInterval(updateBarChart, 1000);
  }

  function updateBarChart(){
     d3.select(chartSelector).selectAll("text").remove();

     var svg = d3.select(chartSelector)
                    .append("text")
                    .attr("width", 100)
                    .attr("height", 100)
                    .text(count);
  }

  function addGeoData(data) {
    updateCount();
  }

  function updateCount() {
    count += 1;
  }

  return {
    addGeoData: addGeoData
  };
}

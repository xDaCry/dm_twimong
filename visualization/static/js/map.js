function worldMap(mapSelector, colors) {
  var geoData = [];

  var width = 750,
      height = 400,
      translate = [width / 2, height / 2];

  var projection = d3.geo.equirectangular()
        .scale(115)
        .translate(translate);
  var startPingRadius = 2,
      endPingRadius = 5,
      pingThickness = 0.5;
  var arc = d3.svg.arc()
        .outerRadius(startPingRadius)
        .innerRadius(startPingRadius - pingThickness);
  var svg;

  createMap(mapSelector);

  function createMap(mapSelector) {
    d3.json("/static/geojson/world-50m.json", function(error, world) {
      var path = d3.geo.path()
        .projection(projection);

      svg = d3.select(mapSelector)
        .append("svg")
        .attr("width", width)
        .attr("height", height);

      svg.append("path")
        .datum(topojson.feature(world, world.objects.land))
        .attr("class", "land")
        .attr("d", path);

      svg.append("path")
        .datum(topojson.mesh(world, world.objects.countries))
        .attr("class", "boundary")
        .attr("d", path);
    });
  }
  function addGeoData(data) {
    geoData.push(data);
    updateDots();
  }

  function updateDots() {
    if (!svg) return;

    // enter
    svg.selectAll("circle")
      .data(geoData)
      .enter()
        .append("circle")
        .classed("point", true)
        .attr("r", 3)
        .each(function(d) {
          radarPing(d);
        });

    // update
    svg.selectAll("circle.point")
      .data(geoData)
        .attr("cx", function(d) {
          return projection([d.coordinates.coordinates[0], d.coordinates.coordinates[1]])[0];
        })
        .attr("cy", function(d) {
          return projection([d.coordinates.coordinates[0], d.coordinates.coordinates[1]])[1];
        })
        //.attr("fill", "yellow");
        .attr("fill", countryFill);
  }

  function countryFill(d) {
    return colors(d.lang);
  }

  // Based on the ripples function in
  // https://github.com/NickQiZhu/d3-cookbook/blob/master/src/chapter10/touch.html
  function radarPing(d) {
    var p = projection([d.coordinates.coordinates[0], d.coordinates.coordinates[1]]);
    var x = p[0];
    var y = p[1];
    for (var i = 1; i < 5; i += 1) {
      svg.append("circle")
          .classed("radar-ping", true)
          .attr("cx", x)
          .attr("cy", y)
          .attr("r", startPingRadius - (pingThickness / 2))
          .style("stroke-width", pingThickness / i)
          .style('stroke', countryFill(d))
          //.style('stroke', "white")
        .transition()
          .delay(Math.pow(i, 2.5) * 50)
          .duration(1000).ease('quad-in')
          .attr("r", endPingRadius)
          .style("stroke-opacity", 0)
          .style('stroke', countryFill(d))
          //.style('stroke', "yellow")
          .each("end", function() {
              d3.select(this).remove();
          });
    }
  }

  return {
    addGeoData: addGeoData
};
}

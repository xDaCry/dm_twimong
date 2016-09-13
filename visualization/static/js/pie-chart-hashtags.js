function hashtagsCountPieChart(barChartSelector, colors) {
  var countryCount = {};
  var width = 250;
  var height = 150;
  var transitionDuration = 500;
  var exitTransitionDuration = 500;
  var xScale, yScale;
  var svg;

  createBarChart(barChartSelector);

  function createBarChart(barChartSelector) {
    createChart(barChartSelector);
    createScale();
    startBarChartUpdateTimer();
  }

  function createChart() {
    svg = d3.select(barChartSelector)
      .append('svg')
      .attr('width', width)
      .attr('height', height);
  }

  function createScale() {
    xScale = d3.scale.ordinal()
      .rangeRoundBands([0, width], 0.05);
    yScale = d3.scale.linear()
      .range([0, height]);
  }

  function startBarChartUpdateTimer() {
    setInterval(updateBarChart, 1000);
  }

  function updateBarChart() {
    var dataSet = createBarChartDataSet();
    dataSet = pickTop2(dataSet);
    updateScales(dataSet);
    updateBars(dataSet);
    updateBarLabels(dataSet);
  }

  function pickTop2(dataSet) {
    dataSet.sort(sortDataSet);
    return dataSet.slice(0, 2);
  }

  function sortDataSet(a, b) {
    if (a.count < b.count) {
      return 1;
    }
    if (a.count > b.count) {
      return -1;
    }
    return 0;
  }

  function createBarChartDataSet() {
    var dataSet = [];
    Object.keys(countryCount).forEach(function(hashtags) {
      dataSet.push({
        hashtags: hashtags,
        count: countryCount[hashtags]
      });
    });
    return dataSet;
  }

  function updateScales(dataSet) {
    xScale.domain(d3.range(dataSet.length));
    yScale.domain([0, d3.max(dataSet, function(d) { return d.count; })]);
  }

  function updateBars(dataSet) {
    // select
    var bars = svg.selectAll('rect')
      .data(dataSet, key);

    // enter
    bars.enter()
      .append('rect')
      // .classed('bar', true)
      .attr('x', width) // enter stage right
      .attr('y', height) // rise from zero height
      .attr('width', xScale.rangeBand())
      .attr('height', barHeight)
      .attr('fill', function(d) {
        var c = colors(d.hashtags);
        return d3.rgb(c).brighter(0.1);
      })
      .attr('stroke', function(d) {
        var c = colors(d.hashtags);
        return d3.rgb(c).darker(0.5);
      });

    // update
    bars.transition()
      .duration(transitionDuration)
      .attr('x', function(d, i) {
        return xScale(i);
      })
      .attr('y', function(d) {
        return height - barHeight(d);
      })
      .attr('width', xScale.rangeBand())
      .attr('height', barHeight);

    // exit
    bars.exit()
      .transition()
      .duration(exitTransitionDuration)
      .attr('opacity', 0)
      .remove();
  }

  function barHeight(d) {
    return Math.max(minimumBarHeight(), yScale(d.count));
  }

  function minimumBarHeight() {
    return 20;
  }

  function updateBarLabels(dataSet) {
    // select
    var labels = svg.selectAll('text')
      .data(dataSet, key);

    // enter
    labels.enter()
      .append('text')
      .text(function(d) {
        return d.hashtags;
      })
      .attr('x', function(d, i) {
        return xScale(i) + xScale.rangeBand() / 2;
      })
      .attr('y', function(d) {
        return height - barHeight(d) + 14;
      })
      .attr('text-anchor', 'middle')
      .attr('font-family', 'sans-serif')
      .attr('font-size', '11px')
      .attr('fill', 'white');

    // update
    labels.transition()
      .duration(transitionDuration)
      .attr('x', function(d, i) {
        return xScale(i) + xScale.rangeBand() / 2;
      })
      .attr('y', function(d) {
        return height - barHeight(d) + 14;
      });

    // exit
    labels.exit()
      .transition()
      .duration(exitTransitionDuration)
      .attr('opacity', 0)
      .remove();
  }

  var key = function(d) {
    return d.hashtags;
  };

  function addGeoData(data) {
    updateCountryCount(data.hashtags);
  }

  function updateCountryCount(hashtags) {
    var count = 0;
    if (countryCount[hashtags]) {
      count = countryCount[hashtags];
    }
    count += 1;
    countryCount[hashtags] = count;
  }

  return {
    addGeoData: addGeoData
  };
}

//var json = {"nodes":[{"name":"Myriel","group":1},{"name":"Napoleon","group":1},], "links": []};

PX_PER_CHAR = 5;

function convert_pks_to_ids(nodes, links) {
    /* TODO this is O(n^2) and ugly */
    var map = {};
    nodes.forEach(function(entry, index) {
        map[entry.pk] = index;
    });

    var new_links = [];
    links.forEach(function(entry, index, array) {
        array[index].source = map[entry.source];
        array[index].target = map[entry.target];
    });

    return links;
}

var width = 960,
    height = 500

var svg = d3.select("#flow").append("svg")
    .attr("width", width)
    .attr("height", height);

var force = d3.layout.force()
    .gravity(.05)
    .distance(function(d) {
        return d.distance;
    })
    .charge(function(d) {
        return d.charge;   
    })
    .theta(1)
    .linkStrength(function(d) {
        return d.strength;
    })
    .size([width, height]);

d3.json("/flow/" + flowid + ".json", function(error, json) {

  nodes = json.nodes;
  links = convert_pks_to_ids(nodes, json.links);
  force
      .nodes(nodes)
      .links(links)
      .start();

  var link = svg.selectAll(".link")
      .data(links)
    .enter().append("line")
      .attr("class", function(d) {
          return d.class;
      });

  var node = svg.selectAll(".node")
      .data(nodes)
    .enter().append("g")
      .attr("class", "node")
      .call(force.drag);

  node.append("rect")
      .attr("fill", function(d) {return d.color })
      .attr("opacity", 0.5)
      .attr("stroke-width", 1)
      .attr("stroke", function(d) { return d.color })
      .attr("x", function(d) {return (15 + d.name.length * PX_PER_CHAR) / -2})
      .attr("y", "-0.5em")
      .attr("rx", 4)
      .attr("ry", 4)
      .attr("width", function(d) {return 15 + d.name.length * PX_PER_CHAR})
      .attr("height", 16);

  node.append("text")
      .attr("dx", 0)
      .attr("dy", "0.5em")
      .text(function(d) { return d.name });

  force.on("tick", function() {
    link.attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });

    node.attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });
  });
});



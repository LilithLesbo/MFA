


var json;
var cy = (window.cy = cytoscape({
  container: document.getElementById("cy"),

  boxSelectionEnabled: false,
  autounselectify: true,

  style: [{
      selector: "node",
      css: {
        content: "data(id)",
        "text-valign": "center",
        "text-halign": "center",
        height: "60px",
        width: "100px",
        shape: "rectangle",
        "background-color": "data(faveColor)"
      }
    },
    {
      selector: "edge",
      css: {
        "curve-style": "bezier",
        "control-point-step-size": 40,
        "target-arrow-shape": "triangle"
      }
    }
  ],

  elements: {
    nodes: [{
        data: {
          id: "Top",
          faveColor: "#2763c4"
        }
      },
      {
        data: {
          id: "yes",
          faveColor: "#37a32d"
        }
      },
      {
        data: {
          id: "no",
          faveColor: "#2763c4"
        }
      },
      {
        data: {
          id: "Third",
          faveColor: "#2763c4"
        }
      },
      {
        data: {
          id: "Fourth",
          faveColor: "#56a9f7"
        }
      }
    ],
    edges: [{
        data: {
          source: "Top",
          target: "yes"
        }
      },
      {
        data: {
          source: "Top",
          target: "no"
        }
      },
      {
        data: {
          source: "no",
          target: "Third"
        }
      },
      {
        data: {
          source: "Third",
          target: "Fourth"
        }
      },
      {
        data: {
          source: "Fourth",
          target: "Third"
        }
      }
    ]
  },
  layout: {
    name: "dagre"
  }
}));
cy.ready(function() {
  console.log('Nodes:', cy.nodes().jsons());
  console.log('Edges:', cy.edges().jsons());
  console.log('Elements:', cy.elements().jsons());
});

document.getElementById('save').addEventListener('click', function() {
  json = cy.json();
});
document.getElementById('load').addEventListener('click', function() {
  cy.json(json);
});
from dash import Dash, html, Input, Output, State, dcc, ctx
import dash_bootstrap_components as dbc
import dash_cytoscape as cyto
from dash.dependencies import Input, Output, State
import json
from dash.exceptions import PreventUpdate


app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP]) 

cyto.load_extra_layouts()

app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape',
        elements=[
            {"data": {"id": "one", "label": "Node 1"},
              "position": {"x": 108.36750774609206, "y": 102.77884863971336}},
            {"data": {"id": "two", "label": "Node 2"},
              "position": {"x": 18.120515806694662, "y": 104.55883905201571}},
            {"data": {"id": "three", "label": "Node 3"},
              "position": {"x": 46.117522220739254, "y": 38.16324835995146}},
            {"data": {"id": "four", "label": "Node 4"}, 
              "position": {"x": -20.376623094714382, "y": 19.043042639395924}},
            {"data": {"source": "one", "target": "two", "label": "1 to 2",
                "id": "1012d4bc-f3c8-4a78-9ef3-e893d7d41c26"}},
            {"data": {"source": "two", "target": "three", "label": "2 to 3",
                "id": "e520dbd0-4151-46b1-a6ea-9ca553ca1023"}},
            {"data": {"source": "three", "target": "one", "label": "1 to 3", "id": "028b1438-1141-47f1-a208-70d76cfb02cb"}}, {"data": {"source": "three", "target": "four", "label": "3 to 4", "id": "9e269e2e-2127-430a-b3d0-446e0239e313"}}]  ,
        layout={'name': 'preset'}
    ),
    html.Button("Print elements JSONified", id="button-cytoscape"),
    html.Div(id="html-cytoscape"),
])

@app.callback(
    Output("html-cytoscape", "children"),
    [Input("button-cytoscape", "n_clicks")],
    [State("cytoscape", "elements")],
)
def testCytoscape(n_clicks, elements):
    if n_clicks:
        return json.dumps(elements)


if __name__ == '__main__':
    app.run_server(debug=True)
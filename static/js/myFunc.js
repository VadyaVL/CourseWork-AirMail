var AIRMAIL = {}
AIRMAIL.MODELS = {}
AIRMAIL.COLLECTIONS = {}

AIRMAIL.MODELS.PROFILE = Backbone.Model.extend({
    urlRoot:"/api/v1/profile",
    defaults:{
        id:null
    },
    idAttribute: "id",
    validate: function (attr) {
    }
});


function basic_pie(container, x1, x2) {

  var
    d1 = [[0, x1]],
    d2 = [[0, x2]],
    graph;

  graph = Flotr.draw(container, [
    { data : d1, label : 'Листів' },
    { data : d2, label : 'Повідомлень' },
  ], {
    HtmlText : false,
    grid : {
      verticalLines : false,
      horizontalLines : false
    },
    xaxis : { showLabels : false },
    yaxis : { showLabels : false },
    pie : {
      show : true,
      explode : 6
    },
    mouse : { track : true },
    legend : {
      position : 'se',
      backgroundColor : '#D2E8FF'
    }
  });
};
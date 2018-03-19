import Chart from 'chart.js';
import data from '../../weather data/weatherdata.json'


var ctx =  document.getElementById('chart').getContext('2d');
var parent = [];
var child = [];
// for(var i in data[1]) {
//     child.push(data[1][parseInt(i, 10)])
//     parent.push(i);
// }
for(var i = 1; i <= 12; i++) {
    for(var j in data[2009][i]){
        child.push(data[2009][i][j])
        parent.push("");
        // console.log(j, data[2009][i][j])
    }
    parent.pop();
    parent.push(i)

}
console.log(parent)
var myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: parent,
        datasets: [{
            data: child,
            borderWidth: 1
        }]
    },
    options: {
        legend: {
            labels: {
                // This more specific font property overrides the global property
                defaultFontColor: 'red',
                defaultFontSize: 3
            }
        }
    }
})

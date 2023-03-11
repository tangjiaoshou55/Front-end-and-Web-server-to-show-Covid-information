function bar(response){
  let data=JSON.parse(response);
  let x_list=[];
  let y_list=[];
  for (let dic of data){
    x_list.push(dic['location']);
    y_list.push(dic['series_complete_pop_pct']);
  }
  let re=[{
    x: x_list,
    y: y_list,
    type: 'bar'
  }];
  let layout = {
  xaxis: {title: 'Location'},
  yaxis: {title: '% Fully Vaccined'},
  title: 'Fully Vaccined By Location'
}
Plotly.newPlot('barchart',re,layout);
}

function pie(response){
  let data=JSON.parse(response);
  let re=[
  {
    values: data,
    labels: ['Janssen', 'Moderna', 'Pfizer','Unknown'],
    type: 'pie'
  }
];
  let layout={title:'Vaccine Manufacturer Market Share'};
Plotly.newPlot('piechart',re,layout);
}

function getData(){
  ajaxGetRequest('/barchart', bar)
  ajaxGetRequest('/piechart',pie)

}

function line(response){
  let data=JSON.parse(response)
  x_lst=[]
  y_lst=[]
  for (dic of data){
    x_lst.push(dic['date'])
    y_lst.push(dic['series_complete_pop_pct'])
  }
  let re = [{
  x: x_lst,
  y: y_lst,
  type: 'scatter'
}];
  let layout = {
  xaxis: {title: 'Date'},
  yaxis: {title: '% Fully Vaccined'},
  title: '% '+dic['location']+' Of Fully Vaccined By Date'
}
Plotly.newPlot('linechart', re,layout)
}

function GetLocData(){
  let dt=document.getElementById('locText')
  content=JSON.stringify(dt.value)
  ajaxPostRequest('/linechart',content,line)
}
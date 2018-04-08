SignalsPlot = document.getElementById('SignalsPlot');
DiffPlot = document.getElementById('DiffPlot');


function plotpic(){


    stime = $( "#StartTime" ).slider( "value" );
    etime = $( "#EndTime" ).slider( "value" );
    timeres = $( "#TimeRes" ).slider( "value" );
    period = $( "#Period" ).slider( "value" );
    rtoffset = $( "#RxTOffset" ).slider( "value" );
    rfoffset = $( "#RxFOffset" ).slider( "value" );
    bw = $( "#BandWidth" ).slider( "value" );
 

    


    
    $.get( "http://localhost:5000/getSignalGraph?"+
            "stime="+stime+
            "&etime="+etime+
            "&timeres="+timeres+
            "&period="+period+
            "&rtoffset="+rtoffset+
            "&rfoffset="+rfoffset+
            "&rtoffset="+rtoffset+ 
            "&bw="+bw
         ).done(function(data) {
            
            Plotly.newPlot( SignalsPlot, [{
                    x: data.x,
                    y: data.yt
                }],
                {
                    margin: { t: 0 }
                }
            );
            Plotly.plot( SignalsPlot, [{
                    x: data.x,
                    y: data.yr
                }],
                {
                    margin: { t: 0 }
                }
            );
            Plotly.newPlot( DiffPlot, [{
                x: data.x,
                y: data.diff
            }],
            {
                margin: { t: 0 }
            }
            );
          });


}


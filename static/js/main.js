$( function() {

    function make (id,min,max,val){
        $( "#"+id).slider({
                orientation: "vertical",
                range: "min",
                min: min,
                max: max,
                value: val,
                slide: function( event, ui ) {
                    console.log("plotting")
                    plotpic();
                }
            });

    }

    make("StartTime",0,4,0);
    make("EndTime",0,100,27);
    make("TimeRes",1,4,1);
    make("Period",1,15,10);
    make("TxStartTime",0,4,0);
    make("RxTOffset",0,20,3);
    make("RxFOffset",0,10,2);
    make("BandWidth",5,10,2);

  } );


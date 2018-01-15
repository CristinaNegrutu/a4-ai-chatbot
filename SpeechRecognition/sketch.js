function setup(){
    noCanvas();
    let speech=new p5.Speech();
    speech.setLang('ro-RO');
    let speechRec=new p5.SpeechRec('ro-RO',gotSpeech);
    let output_text=select('#output_text');
    let input_text=select('#input_text');
    
    let listen_button=select('#listen');
    listen_button.mousePressed(start_listening);
    let speak_button=select('#speak');
    speak_button.mousePressed(start_speaking);
    
function start_listening(){
    let continuous=true;
    let interim=false;
    speechRec.start(continuous,interim);
}


function gotSpeech(){
    if(speechRec.resultValue){
        let input=speechRec.resultString;
        output_text.html(input)
    }
}

function start_speaking(){
    var text=document.getElementById("input_text").value;
    speech.speak(text);
}
}

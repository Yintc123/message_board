console.log("hi");

let count=1;
let img_url="";
const message_button=document.getElementById("message_button");
const input_message=document.getElementById("input_message");
const input_img=document.getElementById("input_img");
const message_board=document.getElementById("message_board");

message_button.addEventListener("click", ()=>{
    if (input_message.value=="" && input_img.value=="") return;
    create_message_div(input_message.value, count);
    clean_input();
    count++;
})

input_img.addEventListener("change", function(e){
    if(e.target.files.length==0) return;
    const reader=new FileReader();
    reader.addEventListener("load", ()=>{
        img_url=reader.result;
    })
    reader.readAsDataURL(this.files[0])
})

function create_message_div(message){
    reorder_div_message();
    const div_message=document.createElement("div");
    const hr=document.createElement("hr");
    const client=[];
    client.push(create_client_message(message));
    client.push(create_client_img(img_url));
    client.push(hr);
    div_message.className="div_message";
    for (let i=0;i<client.length;i++){
        if(client[i]){
            div_message.appendChild(client[i]);
        }
    }
    message_board.appendChild(div_message);
    div_message.style.order="1";
}

function create_client_message(message){
    if(message==null || message=="")return;
    const client_message=document.createElement("p");
    client_message.className="client_message";
    client_message.textContent=message;
    return client_message;
}

function create_client_img(img){
    if(img==null || img=="")return;
    const client_img=document.createElement("img");
    client_img.className="client_img";
    client_img.src=img;
    return client_img;
}

function reorder_div_message(){
    const div_message=document.getElementsByClassName("div_message");
    for (let i=0;i<div_message.length;i++){
        div_message[i].style.order=(Number(div_message[i].style.order)+1).toString();
    }
}

function clean_input(){
    input_message.value="";
    input_img.value="";
    img_url="";
}
console.log("hi");

let img_url="";
let img_file=null;
const message_button=document.getElementById("message_button");
const input_message=document.getElementById("input_message");
const input_img=document.getElementById("input_img");
const message_board=document.getElementById("message_board");

function init(){
    import("./message_module.js").then(func=>{
        func.get_message().then(result=>{
            console.log(result);
            for(let i=0;i<result["history"].length;i++){
                create_message_div(result["history"][i]["name"],
                                   result["history"][i]["text_message"], 
                                   result["history"][i]["img_url"]);
            }
        }).then(()=>{
            loading(0);
        });
    })
}

message_button.addEventListener("click", ()=>{
    const input_name=document.getElementById("input_name");
    loading(1);
    if (input_message.value=="" && input_img.value==""){
        loading(0);
        return;
    } 
    create_message_div(input_name.value, input_message.value, null); 
    import("./message_module.js").then(func=>{
        func.send_message(input_name.value, input_message.value, img_file);
        clean_input();
    }).then(()=>{
        loading(0);
    })
})

input_img.addEventListener("change", function(e){
    if(e.target.files.length==0) return;
    // console.log(e.target.files[0]);
    img_file=e.target.files[0];
    const reader=new FileReader();
    reader.addEventListener("load", ()=>{
        img_url=reader.result;
    })
    reader.readAsDataURL(this.files[0])
})

function create_message_div(name, message, img){
    reorder_div_message();
    const div_message=document.createElement("div");
    const hr=document.createElement("hr");
    const client=[];
    client.push(create_client_name(name));
    client.push(create_client_message(message));
    if (img){
        client.push(create_client_img(img));
    }else{
        client.push(create_client_img(img_url));
    }
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

function create_client_name(name){
    if(name=="" || name==null){
        name="匿名";
    }
    const client_name=document.createElement("p");
    client_name.className="client_name";
    client_name.textContent=name + "：";
    return client_name;
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
    img_file=null;
}

function loading(flag){
    const loading_for_confirmation=document.getElementById("loading_for_confirmation");
    if(flag==0){
        loading_for_confirmation.style.display="none";
    }else{
        loading_for_confirmation.style.display="inline-block";
    }
}

init();
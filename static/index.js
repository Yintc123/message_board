console.log("hi");

let img_url="";
let img_file=null;
let flag=0;
let data=[];
const message_button=document.getElementById("message_button");
const input_message=document.getElementById("input_message");
const input_img=document.getElementById("input_img");
const message_board=document.getElementById("message_board");

function init(){
    import("./message_module.js").then(func=>{
        func.get_message().then(result=>{
            for(let i=0;i<result["history"].length;i++){
                create_message_div(result["history"][i]["name"],
                                   result["history"][i]["text_message"], 
                                   result["history"][i]["img_url"],
                                   flag
                                   );
                waiting(flag);
                flag++;
            }
            data=result["history"];
            return result["history"];
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
    create_message_div(input_name.value, input_message.value, null, flag);
    flag++; 
    import("./message_module.js").then(func=>{
        func.send_message(input_name.value, input_message.value, img_file).then(result=>{
            data.push(result);
        }).then(()=>{
            waiting(flag-1);
        });
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

function create_message_div(name, message, img, index){
    reorder_div_message();
    const div_message=document.createElement("div");
    const hr=document.createElement("hr");
    const client=[];
    client.push(create_delete_img(index));
    client.push(create_client_name(name));
    client.push(create_client_message(message));
    if (img){
        client.push(create_client_img(img));
    }else{
        client.push(create_client_img(img_url));
    }
    client.push(hr);
    div_message.className="div_message";
    div_message.id="div"+index;
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

function create_delete_img(index){
    const delete_div=document.createElement("div");
    const delete_img=document.createElement("img");
    delete_div.className="can_div";
    delete_img.className="can";
    delete_img.id="can"+index;
    delete_img.src="./static/icon_delete.png";
    delete_img.style.cursor="not-allowed";
    delete_img.addEventListener("click", ()=>{
        loading(1);
        if (delete_img.style.cursor=="not-allowed"){
            console.log("等待資料傳送至資料庫");
            loading(0);
            return;
        }
        import('./message_module.js').then(func=>{
            const id=index;
            func.delete_message(data[index]["id"]);
            remove_message_div(id);
        }).then(()=>{
            loading(0);
        })
    })
    delete_div.appendChild(delete_img);
    return delete_div;
}

function reorder_div_message(){
    const div_message=document.getElementsByClassName("div_message");
    for (let i=0;i<div_message.length;i++){
        div_message[i].style.order=(Number(div_message[i].style.order)+1).toString();
    }
}

function remove_message_div(index){
    const div_name="div"+index;
    const div_message=document.getElementById(div_name);
    const message_board=document.getElementById("message_board");
    message_board.removeChild(div_message);
}

function clean_input(){
    input_message.value="";
    input_img.value="";
    img_url="";
    img_file=null;
}

function loading(loading_flag){
    const loading_for_confirmation=document.getElementById("loading_for_confirmation");
    if(loading_flag==0){
        loading_for_confirmation.style.display="none";
    }else{
        loading_for_confirmation.style.display="inline-block";
    }
}

function waiting(can_index){
    const can_name="can"+can_index
    const can=document.getElementById(can_name);
    can.style.cursor="pointer";
}

init();
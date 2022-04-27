import {url_mode} from './package.js';

const url=url_mode["url_api_message"];

export async function send_message(img){
    const input_message=document.getElementById("input_message").value;
    console.log(input_message)
    console.log(img)
    let form=new FormData();
    const input=[input_message, img];
    const query=["message", "img"];
    for(let i=0;i<input.length;i++){
        form.append(query[i], input[i]);
    }
    return await fetch(url, {
        method:"POST",
        body:form
    }).then(response=>{
        return response.json();
    })
}

export async function get_message(){
    return await fetch(url).then(response=>{
        return response.json();
    })
}
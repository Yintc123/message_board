import {url_mode} from './package.js';

const url=url_mode["url_api_message"];

export async function send_message(name, text, img){
    let form=new FormData();
    const input=[name, text, img];
    const query=["name", "message", "img"];
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

export async function delete_message(message_id){
    let form=new FormData();
    const id=message_id;
    const query="id";
    form.append(query, id);
    return await fetch(url, {
        method:"DELETE",
        body:form
    }).then(response=>{
        return response.json();
    })
}
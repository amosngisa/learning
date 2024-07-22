import React, { useState } from "react";
import { v4 as uuidv4 } from 'uuid';

const App = () => {

    console.log('Render: App');

    const [users, setUsers] = useState([{id: 'a', name: 'Joan Mwangi'}, {id: 'b', name: 'Shawn Paul'}]);
    const [text, setText] = useState('');

    const handleText = (event) =>{
        setText(event.target.value);
    }

    const handleAdduser = () => {
        setUsers(users.concat({id: uuidv4(), name: text}));
    }

    const handleRemove = (id) => {
        setUsers(users.filter((user) => user.id !== id));
    }

    return(
        <div>
            <input type="text" value={text} onChange={handleText} />
            <button type="button" onClick={handleAdduser}>Add User</button>
            <List list={users} onRemove={handleRemove} />
        </div>
    )

}

const List = React.memo(({list, onRemove}) => {
    console.log('Render: List');

    return(
        <ul>
            {list.map((item) => (
                <ListItem key={item.id} item={item} onRemove={onRemove} />
            ))}
        </ul>
    );
});


const ListItem = React.memo(({item, onRemove}) => {
    console.log('Render: ListItem')
    return (
        <li>
            {item.name}
            <button type="button" onClick={() => onRemove(item.id)}>Remove</button>
        </li>
    );
});
    
    



export default App
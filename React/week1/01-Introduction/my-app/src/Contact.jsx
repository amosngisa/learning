import {NavLink, Outlet} from 'react-router-dom';

export const Contact = ()=>{
    return(
        <div>
            <div className='ContactOption'>
                <NavLink to="search">Search</NavLink>
                <NavLink to="friends">Friend</NavLink>
                <NavLink to="request">Request</NavLink>
                <NavLink to="stranger">Stranger</NavLink>
            </div>

            <Outlet />

        </div>
    )
}


export const Contacts = ()=>{
    return(
        <div>
            <div className='ContactOption'>
                <NavLink to="search">Search</NavLink>
                <NavLink to="friends">Friend</NavLink>
                <NavLink to="request">Request</NavLink>
                <NavLink to="stranger">Stranger</NavLink>
            </div>

            <Outlet />

        </div>
    )
}


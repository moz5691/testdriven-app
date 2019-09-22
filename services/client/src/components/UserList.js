import React from 'react';

const UserList = (props) => (
  <div>
    {
      props.users.map((user) => (
        <h4 key={user.id} className='box title is-4'>
            {user.username}
        </h4>
      ))
    }
  </div>
)

export default UserList;
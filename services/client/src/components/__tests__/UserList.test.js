import {shallow} from 'enzyme';
import React from 'react';
import renderer from 'react-test-renderer';

import UserList from '../UserList';

const users = [
  {
    'active': true,
    'email': 'michael@gmail.com',
    'id': 1,
    'username': 'michael',
  },
  {
    'active': true,
    'email': 'jonnykay@gmail.com',
    'id': 2,
    'username': 'jonny1',
  }
];

test('UserList renders properly', () => {
  const wrapper =
      shallow(
          <UserList users =
           {
             users
           } />);
  const element = wrapper.find('h4');
  expect(element.length).toBe(2);
  expect(element.get(0).props.children).toBe('michael');
});

test('userList renders a snapshot properly', ()=>{
  const tree = renderer.create(<UserList users={users}/>)
          .toJSON();
  expect(tree).toMatchSnapshot();
});
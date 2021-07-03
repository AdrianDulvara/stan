import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Category from '../views/Category.vue'
import Product from '../views/Product.vue'
import Search from '../views/Search.vue'
import Cart from '../views/Cart.vue'
import Favourites from "../views/Favourites.vue"
import SignUp from "../views/SignUp.vue"
import Login from "../views/Login.vue"

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path:"/login",
    name: 'login',
    component: Login
  },
  {
    path:"/signup",
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
{
    path:'/cart',
    name:'Cart',
    component: Cart
  },
  {
    path:'/favourites',
    name:'Favourites',
    component: Favourites
  },
  {
    path: '/:category_slug/',
    name: 'Category',
    component: Category
  },
  {
    path: '/:category_slug/:product_slug/',
    name: 'Product',
    component: Product
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router

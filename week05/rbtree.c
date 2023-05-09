void rbtree_insert_fix(rbtree *t, node_t *z) {
    while (z->parent->color == RBTREE_RED) {
    // 부모와 삼촌이 둘 다 red일 때 case. 1
        node_t *y = z->parent->parent->left;
        if (z->parent->parent->left->color == RBTREE_RED && z->parent->parent->right->color == RBTREE_RED){
            // y = uncle
            if (z->parent == z->parent->parent->left) {
                y = z->parent->parent->right;
            }

            z->parent->color = RBTREE_BLACK;
            y->color = RBTREE_BLACK;
            z->parent->parent->color = RBTREE_RED;
            z = z->parent->parent;
        }
        // 삼촌이 검정색 일때 case. 2 or case. 3
        // 부모가 할아버지의 왼쪽 자식일 때
        else if (z->parent == z->parent->parent->left) {
            // 부모의 오른쪽 자식일 때 case. 2
            if (z == z->parent->right) {
                z = z->parent;
                left_rotate(t, z);
            }
            // case. 3
            z->parent->color = RBTREE_BLACK;
            z->parent->parent->color = RBTREE_RED;
            right_rotate(t, z->parent->parent);
        }
        // 부모가 할아버지의 오른쪽 자식일 때
        else {
            // 부모의 왼쪽 자식일 때 case. 2
            if (z == z->parent->left) {
                z = z->parent;
                right_rotate(t, z);
            }
            // case. 3
            z->parent->color = RBTREE_BLACK;
            z->parent->parent->color = RBTREE_RED;
            left_rotate(t, z->parent->parent);
        }
    }
}
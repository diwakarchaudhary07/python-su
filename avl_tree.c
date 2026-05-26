// AVL Tree Program in C
// Insertion and Traversal

#include <stdio.h>
#include <stdlib.h>

// AVL Node Structure
struct Node
{
    int data;
    struct Node *left;
    struct Node *right;
    int height;
};

// Function to get height
int height(struct Node *N)
{
    if (N == NULL)
        return 0;

    return N->height;
}

// Maximum of two numbers
int max(int a, int b)
{
    return (a > b) ? a : b;
}

// Create new node
struct Node* createNode(int value)
{
    struct Node* node =
        (struct Node*)malloc(sizeof(struct Node));

    node->data = value;
    node->left = NULL;
    node->right = NULL;
    node->height = 1;

    return node;
}

// Right Rotate
struct Node* rightRotate(struct Node *y)
{
    struct Node *x = y->left;
    struct Node *T2 = x->right;

    x->right = y;
    y->left = T2;

    y->height = max(height(y->left),
                    height(y->right)) + 1;

    x->height = max(height(x->left),
                    height(x->right)) + 1;

    return x;
}

// Left Rotate
struct Node* leftRotate(struct Node *x)
{
    struct Node *y = x->right;
    struct Node *T2 = y->left;

    y->left = x;
    x->right = T2;

    x->height = max(height(x->left),
                    height(x->right)) + 1;

    y->height = max(height(y->left),
                    height(y->right)) + 1;

    return y;
}

// Get Balance Factor
int getBalance(struct Node *N)
{
    if (N == NULL)
        return 0;

    return height(N->left) - height(N->right);
}

// Insert Node
struct Node* insert(struct Node* node, int value)
{
    // Normal BST Insertion
    if (node == NULL)
        return createNode(value);

    if (value < node->data)
        node->left = insert(node->left, value);

    else if (value > node->data)
        node->right = insert(node->right, value);

    else
        return node;

    // Update height
    node->height = 1 + max(height(node->left),
                           height(node->right));

    // Get balance factor
    int balance = getBalance(node);

    // Left Left Case
    if (balance > 1 && value < node->left->data)
        return rightRotate(node);

    // Right Right Case
    if (balance < -1 && value > node->right->data)
        return leftRotate(node);

    // Left Right Case
    if (balance > 1 && value > node->left->data)
    {
        node->left = leftRotate(node->left);
        return rightRotate(node);
    }

    // Right Left Case
    if (balance < -1 && value < node->right->data)
    {
        node->right = rightRotate(node->right);
        return leftRotate(node);
    }

    return node;
}

// Preorder Traversal
void preorder(struct Node *root)
{
    if(root != NULL)
    {
        printf("%d ", root->data);
        preorder(root->left);
        preorder(root->right);
    }
}

// Main Function
int main()
{
    struct Node *root = NULL;

    root = insert(root, 10);
    root = insert(root, 20);
    root = insert(root, 30);
    root = insert(root, 40);
    root = insert(root, 50);
    root = insert(root, 25);

    printf("Preorder Traversal of AVL Tree:\n");
    preorder(root);

    return 0;
}
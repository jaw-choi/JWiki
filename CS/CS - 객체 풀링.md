
- **개선된 코드:**
    
    ```cpp
    #include <iostream>
    #include <vector>
    
    class ObjectPool {
    public:
        ObjectPool(int size) {
            objects.resize(size);
            for (int i = 0; i < size; ++i) {
                available.push_back(&objects[i]);
            }
        }
    
        GameObject* GetObject() {
            if (available.empty()) {
                return nullptr; // 풀에 객체가 없으면 nullptr 반환
            }
            GameObject* obj = available.back();
            available.pop_back();
            return obj;
        }
    
        void ReturnObject(GameObject* obj) {
            available.push_back(obj);
        }
    
    private:
        std::vector<GameObject> objects;
        std::vector<GameObject*> available;
    };
    
    int main() {
        ObjectPool pool(10);
        GameObject* obj = pool.GetObject();
        if (obj) {
            // 객체 사용
            pool.ReturnObject(obj);
        }
        return 0;
    }
    ```
    
- **성능 최적화:**
    
    - 객체 풀링은 객체 생성 및 삭제 비용을 줄여 성능을 향상시킬 수 있습니다.
    - 자주 사용되는 객체를 미리 생성해두고 재사용하는 방식으로 메모리 할당 및 해제 빈도를 줄입니다.

## 이 코드에서 배운점

1. **객체 풀링의 효과:** 객체 생성 및 삭제 비용을 줄이기 위해 객체 풀링을 사용할 수 있습니다. 객체 풀링은 메모리 할당 및 해제 빈도를 줄여 성능을 향상시킬 수 있습니다.

2. **객체 풀링 사용:** 자주 사용되는 객체를 미리 생성해두고 재사용하는 방식으로 메모리 할당 및 해제 빈도를 줄입니다.
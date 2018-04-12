/*
 *
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 *
*/
package org.apache.airavata.registry.core.entities.appcatalog;

import java.io.Serializable;

/**
 * The primary key class for the compute_resource_policy database table.
 *
 */
public class ComputeResourcePolicyPK implements Serializable {

    private static final long serialVersionUID = 1L;

    private String resourcePolicyId;

    public ComputeResourcePolicyPK() {
    }

    public String getResourcePolicyId() {
        return resourcePolicyId;
    }

    public void setResourcePolicyId(String resourcePolicyId) {
        this.resourcePolicyId = resourcePolicyId;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        ComputeResourcePolicyPK that = (ComputeResourcePolicyPK) o;

        return resourcePolicyId != null ? resourcePolicyId.equals(that.resourcePolicyId) : that.resourcePolicyId == null;
    }

    @Override
    public int hashCode() {
        return resourcePolicyId != null ? resourcePolicyId.hashCode() : 0;
    }
}